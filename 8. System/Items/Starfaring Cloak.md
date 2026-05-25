---
type: item
source-type: "Remaster"
level: "24"
traits: ["[[Artifact]]", "[[Divine]]", "[[Invested]]", "[[Light]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The swirling folds of a *starfaring cloak* appear to contain the night sky, with the stars rotating hypnotically through its firmament shedding dim light to a range of 10 feet. While wearing the cloak, you gain a +10-foot item bonus to your Speed and a fly Speed equal to your Speed. You can survive comfortably without breathing, in the void of space, and in severe or extreme cold or heat. Also, you gain sustenance from starlight and sunlight, so if you're outdoors for an hour or more per day, you don't need to eat or drink. While wearing the cloak, you can navigate perfectly and unerringly by looking up at the sky.

**Activate** R (concentrate, fortune)

**Frequency** once per day

**Trigger** You make an attack roll, skill check, or saving throw

**Effect** Reroll the triggering roll and take the higher result. This is a fortune effect.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The cloak casts [[Sleep]] at 4th rank (DC 42).

**Activate** `pf2:3` (concentrate)

**Frequency** once per week

**Effect** The cloak casts [[Teleport]] at 10th rank. If you name no destination, it teleports you to a random planet in a random location that's safe for you.

**Destruction** If the wearer of a *starfaring cloak* is bound by [[Imprisonment]] for a century and a day, the cloak dissolves into light. This time is reduced to a year and a day if the wearer is placed in eternal slumber by *imprisonment* and subjected to the [[Nightmare]] spell once per day.

**Source:** `= this.source` (`= this.source-type`)
