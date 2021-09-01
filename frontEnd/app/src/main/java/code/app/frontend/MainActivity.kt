package code.app.frontend

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    val tiendas=listOf(
        Tienda(nombreTienda = "Futeria Rosita",imagen = "https://cursokotlin.com/wp-content/uploads/2017/07/spiderman.jpg"),
        Tienda(nombreTienda = "Los Tres Hermanos", imagen = "https://www.flickr.com/photos/193825847@N03/51417413175/in/dateposted-public/")
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        initRecycler()
    }
    fun initRecycler(){
        rvTienda.layoutManager=LinearLayoutManager( this)
        val adapter=TiendaAdapter(tiendas)
        rvTienda.adapter=adapter
    }
}