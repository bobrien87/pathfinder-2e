---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 210}"
usage: "worn"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Sure-step crampons* are sturdy leather boots with warm fur lining and magically augmented steel crampons that offer the wearer purchase on even the slipperiest ice slicks. They allow you to walk across ice without difficulty, ignoring the uneven ground and difficult terrain caused by ice, and reducing greater difficult terrain caused by ice to difficult terrain.

**Activate** `pf2:1` (manipulate)

**Requirements** You're standing on an earthen, icy, or wooden surface

**Effect** You dig the crampons into the spot where you're standing, offering additional support until the next time you move. You gain a +2 circumstance bonus to your Fortitude and Reflex DCs against attempts to [[Shove]] or [[Trip]] you. This bonus also applies to saving throws against spells or effects that attempt to move you or knock you [[Prone]]. The bonus lasts until you move from your current spot.

**Source:** `= this.source` (`= this.source-type`)
