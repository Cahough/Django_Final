class my_buttons:

	def get_buttons:
		button =  """<style>
		.button-container form,
		.button-container form div{
        		display: inline;
		}

		.button-container button {
        		display: inline;
        		vertical-align: middle;
		}
		</style>
		<h1>put in what you know and press search</h1>
		<div class="button-container">
		<form action="http://127.0.0.1:8000/search">
        		<div>
                		<button type="submit"> search page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000/add">
        		<div>
                		<button type="submit">add page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000">
        		<div>
                		<button type="submit">home page</button>
        		</div>
		</form>
		<form action="http://127.0.0.1:8000/list">
        		<div>
                		<button type="submit">show contacts</button>
        		</div>
		</form>
		</div>"""
	
		return button
		
