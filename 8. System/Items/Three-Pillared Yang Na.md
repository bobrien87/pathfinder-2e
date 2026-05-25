---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Divine]]", "[[Invested]]", "[[Tattoo]]"]
price: "{'gp': 80}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tattoo represents an abstract tree whose trunk is made up of three lines of Tang text. Applied in a ritual involving jasmine, turmeric, and a blossom from a yang na tree, the tattoo provides three blessings. The first blessing keeps your mind still during negotiations, granting a +1 item bonus to Diplomacy checks.

**Activate—Second Blessing** `pf2:1` (concentrate, detection)

**Effect** You learn the direction of the yang na tree that gave the blossom used in creating your tattoo. Most such trees are in Tang Mai, far to the west of the Inner Sea.

**Activate—Third Blessing** `pf2:r` (concentrate)

**Trigger** You take spirit damage

**Effect** You gain resistance 3 against that spirit damage.

**Source:** `= this.source` (`= this.source-type`)
