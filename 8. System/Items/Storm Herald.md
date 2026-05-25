---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Deadly d6]]", "[[Electricity]]", "[[Finesse]]", "[[Magical]]", "[[Monk]]", "[[Sonic]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This iridescent, black *+2 striking [[Shock]] [[Thundering]] fighting fan* is crafted from the crackling feathers of thunderbirds to resemble one of the beast's mighty wings. Channeling the avian's tempestuous nature, you are surrounded by a stormy shell of wind and electricity while wielding a *storm herald*, granting you resistance 5 to electricity and sonic damage.

**Activate—Call the Storm** `pf2:2` (concentrate, magical, manipulate)

**Frequency** once per day

**Effect** You channel the full might of a storm with you as its epicenter. All creatures within @Template[emanation|distance:30]{30 feet} take @Damage[3d10[electricity],3d10[sonic]|options:area-damage]{3d10 electricity damage and 3d10 sonic damage} (DC 30 [[Reflex]] save).

**Craft Requirements** The initial raw materials must include feathers from a thunderbird.

**Source:** `= this.source` (`= this.source-type`)
