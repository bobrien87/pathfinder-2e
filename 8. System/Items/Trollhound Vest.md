---
type: item
source-type: "Remaster"
level: "6"
price: "{'gp': 230}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+1 hide armor* is sickly green and covered in thick warts and nodules, fashioned from the hide of a trollhound and imbued with some of the beast's vitality. Wearing this armor gives you a –1 circumstance penalty to all checks made using Diplomacy to interact with trolls and a +1 circumstance bonus to Diplomacy checks used to [[Make an Impression]] in communities traditionally plagued by troll attacks.

**Activate** `pf2:r` (manipulate)

**Trigger** You take damage from a melee attack while you have half or fewer of your normal maximum Hit Points

**Effect** Your body knits itself back together, healing you for 3d8 healing Hit Points.

**Craft Requirements** The initial raw materials must include the hides of at least two trollhounds.

**Source:** `= this.source` (`= this.source-type`)
