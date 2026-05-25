---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 850}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Placed under the eyes like rays of light, this tattoo burns away illusions with the unmerciful brilliance of the sun. You gain a +2 bonus to Perception checks that involve sight. If you're [[Dazzled]], you receive a new save at the start of each of your turns to end your dazzled condition.

**Activate** `pf2:1` to `pf2:3` (concentrate)

**Frequency** once per day

**Effect** The tattoo casts a 4th-rank [[Blazing Bolt]], with the rays emitting from your eyes. The number of actions you spend Activating the tattoo determines *blazing bolt*'s number of rays. The tattoo also attempts to dispel each illusion on a creature hit by a ray (counteract rank 5th, counteract modifier +19).

**Source:** `= this.source` (`= this.source-type`)
