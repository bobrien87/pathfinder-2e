---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 5000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Though it contains but a tiny drop of Gorum's blood, drinking this thick, swirling potion fills the user with divine wrath and resilience. While under the effect of the potion, you gain a +4 status bonus to physical damage rolls for 1 minute.

> [!danger] Effect: Crimson Godsblood Serum

The first time during that minute you're reduced to 0 Hit Points but not immediately killed, you avoid being knocked out, regain @Damage[(6d8+20)[healing]] Hit Points, and become [[Confused]] for 1 round, and your [[Wounded]] condition increases by 1.

**Source:** `= this.source` (`= this.source-type`)
