---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your hands fit through the venomous mouths of this pair of handwraps made from amphisbaena skin. Your unarmed strikes gain the versatile P trait. *Amphisbaena handwraps* can have weapon runes etched onto them, similar to [[Handwraps of Mighty Blows]].

**Activate—Twin Venom Strike** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** Make two unarmed Strikes. Both Strikes count toward your multiple attack penalty, but the penalty doesn't increase until after both attacks. Each Strike deals an additional 1d6 poison damage.

**Craft Requirements** The initial raw materials must include the skin and heads of an amphisbaena.

**Source:** `= this.source` (`= this.source-type`)
