---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This copper tripod has a magical core that can't be moved once magically locked in place—a perfect example of engineering ingenuity applied to magic items. This eccentric magical power is put to a pragmatic use of stabilizing weapons without the need for solid ground on which to stabilize them. In addition to extraplanar and aquatic environments, these devices have seen use by flying and climbing snipers who would otherwise have no way to mitigate their weapons' fierce kickback.

**Activate** `pf2:1` (manipulate)

**Effect** You deploy the tripod and press a button to lock it into place, allowing you to deploy the tripod in midair, underwater, or anywhere else where you don't have a solid horizontal surface available. If you Activate the tripod by pushing the button again, you release and retrieve the tripod. While anchored, the tripod can be moved only if 8,000 pounds of pressure are applied to it or if a creature uses Athletics to `act force-open` the tripod with a DC of 40 (though most intelligent creatures can just push the button to release the tripod).

**Source:** `= this.source` (`= this.source-type`)
