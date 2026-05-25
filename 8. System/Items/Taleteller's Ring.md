---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "wornring"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Smiling faces are inscribed about this silver band. You become a fluent weaver of fictions, gaining a +2 item bonus to Deception checks to [[Lie]], Deception DCs against `act sense-motive`, and Performance checks for storytelling. Whenever you're under suspicion or being questioned by an authority figure, you find yourself compulsively spinning absurd, tall tales that are so unconvincing that they make you look guilty even when you're innocent. The ring's bonuses vanish, and any listener can quickly determine you're lying. Nevertheless, you're completely unable to be honest in such situations.

**Source:** `= this.source` (`= this.source-type`)
