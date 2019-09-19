datatype  inte = X
            |Z
            |T
            |F
            |S of  inte
            |P of  inte
            |IZ of  inte
            |GTZ of  inte
            |ITEB of  inte *  inte *  inte
            |ITE of  inte *  inte *  inte
            |Abst of inte
            |Appl of inte * inte
            |syntax_error



fun check(S(x))=T
    |check(P(x))=F
    |check(Z)=F
    |check(x)=syntax_error

fun beta(X,y) = y
    |beta(S(x),y)=S(beta(x,y))
    |beta(P(x),y)=P(beta(x,y))
    |beta(IZ(x),y)=IZ(beta(x,y))
    |beta(GTZ(x),y)=GTZ(beta(x,y))
    |beta(ITEB(x,m,n),y)=ITEB(beta(x,y),beta(m,y),beta(n,y))
    |beta(ITE(x,m,n),y)=ITE(beta(x,y),beta(m,y),beta(n,y))
    |beta(Appl(x,z),y)=                        (*confusion lies ahead*)
    let
      val a = beta(x,z)
    in
      beta(a,y)
    end
    |beta(x,y)=x                                (*do something for abst of abst i.e lambda xy[L]*)
            

fun run Z = Z
    |run T =T
    |run F = F

    |run (S(P(x))) = if x=T orelse x=F then syntax_error else run(x)
    |run (P(S(x))) = if x=T orelse x=F then syntax_error else run(x)

    |run (S(x)) =
    let
        val x1=run(x)
    in
      if x1=T orelse x1=F then syntax_error
      else if x1=x then S(x)
      else run(S(x1))
    end

    |run (P(x)) =
    let
        val x1=run(x)
    in
      if x1=x then P(x)
      else run(P(x1))
    end

   

    |run(ITEB(x,y,z))=
    let
      val x1=run(x)
      val y1=run(y)
      val z1=run(z)
    in
      if (not(y1=  T orelse y1= F)) orelse (not(z1= T orelse  z1=F)) then syntax_error
      else if x1=T then y1
      else if x1=F then z1
      else syntax_error
    end
    
    |run(ITE(x,y,z))=
    let
      val x1=run(x)
      val y1=run(y)
      val z1=run(z)
    in
      if (y1= T orelse y1=F) orelse (z1=T orelse z1= F) then syntax_error
      else if x1=T then y1
      else if x1=F then z1
      else syntax_error
    end


    |run (IZ(x))=
    let
      val x1=run(x)
    in
      if(x1=T orelse x1=F) then syntax_error
      else if(x1=Z)then T
      else F
    end

    |run(GTZ(x))=
    let
        val x1=run(x)
    in
         check(x1)
    end

    |run(Appl(Abst(x),y))= run(beta(x,y))
    (* |run(Appl(x,y))= run(beta(x,y)) *)
    (* |run(Abst(x))=Abst(run(x))       Not sure about this *)
    |run(X)=X
    |run (x)= syntax_error
