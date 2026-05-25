---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1300}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As you move your body, qi flows into *mala beads of foresight* you wear and have invested, making them one with your life force. In their usual form, beads are spheres of wood, but versions customized to different martial orders are common. You gain a +2 item bonus to Religion checks.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a divine monk qi spell. If not used by the end of your turn, this Focus Point is lost.

**Activate** `pf2:f` (concentrate)

**Frequency** once per hour

**Requirements** You have just Refocused by meditating

**Effect** While meditating, you searched your feelings for a portent of the future. You're affected by an [[Augury]] spell.

**Craft Requirements** You are a monk with divine qi spells.

**Source:** `= this.source` (`= this.source-type`)
