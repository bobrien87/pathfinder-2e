---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Talisman]]"]
price: "{'gp': 5000}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You lose the [[Dying]] condition

**Requirements** You have a [[Wounded]] value of 1 or more.

This tarnished steel pendant is inlaid with the face of an enraged badger. When you Activate the talisman, it casts a 9th-rank [[Heroism]] on you. If you lose the wounded condition, the *heroism* ends immediately.

**Source:** `= this.source` (`= this.source-type`)
