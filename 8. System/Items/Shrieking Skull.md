---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Auditory]]", "[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 400}"
usage: "affixed-to-crossbow-or-firearm"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a firearm or crossbow

**Activate** a (concentrate)

**Requirements** You're an expert in Intimidation and the affixed weapon is loaded.

This dried skull of a snake is mounted atop the firearm's barrel or affixed to a crossbow's stock. When activated, the skull crawls onto the ammunition loaded in the affixed weapon. If you Strike with the weapon before the end of your turn, the skull lets out a bloodcurdling scream as the ammunition approaches its target. Regardless of whether the Strike is a success, the screaming skull allows you to attempt to [[Demoralize]] the target as well as each enemy within 30 feet of the target.

**Source:** `= this.source` (`= this.source-type`)
