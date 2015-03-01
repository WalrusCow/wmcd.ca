<%inherit file="base.mako"/>

<%block name="content">
<form id="login" action="/login" method="post">
<input required="true" type="text" name="user" placeholder="Username"/>
<br>
<input required="true" type="password" name="password" placeholder="Password"/>
<br>
<input type="submit" value="Submit"/>
</form>
</%block>
