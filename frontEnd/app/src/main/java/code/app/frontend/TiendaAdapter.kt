package code.app.frontend
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.item_tienda.view.*


class TiendaAdapter(val tiendas:List<Tienda>):RecyclerView.Adapter<TiendaAdapter.TiendaHolder>(){


    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TiendaHolder {
        val layoutInflater=LayoutInflater.from(parent.context)
        return TiendaHolder(layoutInflater.inflate(R.layout.item_tienda,parent, false))

    }

    override fun getItemCount(): Int= tiendas.size


    override fun onBindViewHolder(holder: TiendaHolder, position: Int) {
        holder.render(tiendas[position])
    }
    class TiendaHolder(val view:View):RecyclerView.ViewHolder(view){
        fun render(tiendas:Tienda){
            view.tvnombreTienda.text=tiendas.nombreTienda
            Picasso.get().load(tiendas.imagen).into(view.ivTienda)

        }
    }
}