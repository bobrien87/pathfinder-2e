---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 550}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tattoo usually depicts a humanoid skull with staring eyes in its sockets, but any creature with two eyes and a skull is possible, such as a wolf, phoenix, or psychopomp. When your dying condition increases to a value that would kill you, this tattoo reduces your [[Dying]] value to 1 fewer than would kill you. If a death effect would kill you—provided the effect is from a creature of 8th level or lower or a spell of 4th rank or lower—this tattoo activates and keeps you alive instead. You can benefit from this ability only once per day. Each time the tattoo prevents you from dying, one of its eyes disappears, the image now featuring either an empty socket or an eyepatch or other covering. After both eyes vanish, the tattoo becomes non-magical and no longer protects you. If you receive a new staring skull tattoo, any other you have loses its staring eyes and becomes non-magical.

**Source:** `= this.source` (`= this.source-type`)
