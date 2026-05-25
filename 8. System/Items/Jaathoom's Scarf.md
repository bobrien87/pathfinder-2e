---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This scarf is made of fine silk that's the same shade of blue as a clear, cloudless sky. The short ends are edged with a fine gold fringe that seems to sway even in still weather as though touched by invisible winds. The long edges have exquisite embroidery in threads that vary from a blue identical to the silk to the deep gray of storm clouds during winter. Wearing this scarf grants a +2 item bonus to Performance checks to dance and to Acrobatics checks to [[Escape]].

**Activate—Vanish** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The scarf casts 4th-rank [[Invisibility]] on you.

**Activate—Jaathoom's Rebuke** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** You let the winds around you catch the edges of the *jaathoom's scarf*, and a jaathoom shuyookh appears with a sudden updraft. The winds force your enemies back, granting you some breathing room in battle. Each enemy in a @Template[emanation|distance:10] must succeed at a DC 27 [[Fortitude]] save or be pushed 10 feet. A creature that critically fails is also knocked [[Prone]] after being moved. Creatures with the air trait are immune to all these effects.

**Source:** `= this.source` (`= this.source-type`)
