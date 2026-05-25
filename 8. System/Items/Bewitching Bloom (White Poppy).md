---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 80}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While dormant, this tattoo appears to be a simple flower bud, but when activated the flower swiftly blossoms, remaining that way until the next time you make your daily preparations. These blooms are colorful, elegant representations of white poppy flowers.

**Activate** `pf2:2` envision

**Frequency** once per day

**Effect** Choose a willing ally you can see within 30 feet. A sense of peace overwhelms the ally. The tattoo casts [[Calm]] or [[Sanctuary]] (your choice) on the ally. The spell affects only the ally and lasts only until the end of your next turn. Your ally need not be willing if under the control of another creature. However, the controlling creature can attempt a DC 20 [[Will]] save, disrupting your activation on a success.

**Source:** `= this.source` (`= this.source-type`)
