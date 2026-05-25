---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
usage: "attached-to-crossbow-or-firearm-scope"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *scope of truth* is a bit bigger than most to accommodate larger lenses, which have been magically prepared with tiny shards from crystal balls to reveal the truth. The scope grants you a +2 item bonus to Perception checks made to [[Seek]] in areas you can see through the scope.

**Activate—Reveal All** `pf2:2` (manipulate)

**Frequency** Once per day

**Effect** For the next 10 minutes, you can see things through the scope as they actually are. The GM rolls a secret counteract check with a +20 counteract modifier and a counteract rank of 7 against any illusion or polymorph effect in the area, but only for the purpose of determining whether you see through it, not to end the spell or effect. For instance, if the check succeeds against a polymorph spell, you can see the creature's true form, but you don't end the spell.

**Source:** `= this.source` (`= this.source-type`)
