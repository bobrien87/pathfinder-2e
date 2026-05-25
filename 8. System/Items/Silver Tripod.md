---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Force]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 3}"
usage: "affixed-to-firearm-with-the-kickback-trait"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** a (concentrate)

This tiny, silver facsimile of a weapon tripod is usually attached to the underside of the affixed weapon's barrel. When activated, it creates an invisible construct of magical force that attaches to the weapon and automatically stabilizes it in any location, even in midair. The effect lasts for 1 minute or until you Dismiss it. The effect also ends immediately if you let go of the affixed weapon. The affixed weapon cannot be moved while this effect is active.

**Source:** `= this.source` (`= this.source-type`)
