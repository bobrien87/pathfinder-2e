---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'gp': 95}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This finely wrought sextant is made from silver with several onyx mirrors and shades made from thin sets of crystal glass. A fine spyglass made of silver is affixed to the frame; removing the spyglass destroys the sextant. By all appearances, the sextant shouldn't function, as the shades and mirrors are swapped, but when you look through the spyglass, you see a night sky during the day and the sun during the night, as if day and night were inverted. When you use the sextant, you gain a +1 item bonus to Survival checks, which increases to a +2 item bonus when you [[Sense Direction]].

**Source:** `= this.source` (`= this.source-type`)
