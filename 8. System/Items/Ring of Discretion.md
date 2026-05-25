---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Magical]]", "[[Visual]]"]
price: "{'gp': 15}"
usage: "wornring"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *ring of discretion* magically conceals any armor and sheathed weapons you're wearing by either turning them invisible or creating the illusion of ordinary clothes. The ring doesn't change your appearance beyond concealing weapons and armor. As soon as you wield a weapon affected by the ring, the weapon becomes obvious to onlookers and is no longer affected until you sheathe the weapon for at least 1 minute. A creature can use the [[Seek]] action to examine you and disbelieve this illusion (DC 15), and it can attempt to do so without using an action each time it hits you with an attack.

**Source:** `= this.source` (`= this.source-type`)
