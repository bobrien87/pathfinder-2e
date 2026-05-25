---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Fortune]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 1200}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to armor

**Activate** `pf2:f` (concentrate)

**Trigger** You're critically hit by a firearm attack.

This talisman usually takes the form of a small sentimental object carried in a pocket or attached to the inside of a piece of armor. When you activate it, it slows the attack, and you reduce the damage from the triggering critical hit by 10, as the attack destroys the talisman. This effect only reduces the additional damage from a critical hit; it can't reduce the damage below the amount it would deal on a normal hit.

When you activate a *major indomitable keepsake*, you reduce the damage from a firearm critical hit by 30 instead of reducing it by 10.

**Source:** `= this.source` (`= this.source-type`)
