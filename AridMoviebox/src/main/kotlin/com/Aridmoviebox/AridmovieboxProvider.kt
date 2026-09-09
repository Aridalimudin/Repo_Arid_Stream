package com.Aridmoviebox

import com.lagradost.cloudstream3.plugins.BasePlugin
import com.lagradost.cloudstream3.plugins.CloudstreamPlugin

@CloudstreamPlugin
class AridmovieboxProvider: BasePlugin() {
    override fun load() {
        registerMainAPI(Aridmoviebox())
    }
}
