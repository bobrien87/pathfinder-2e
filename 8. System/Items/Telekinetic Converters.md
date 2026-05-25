---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1950}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Copper cables run from these thick leather gloves to nodes that attach to the wearer's temples, allowing a spellcaster to convert the magic they normally cast to pure psychic intention. When you Cast a Spell using the *telekinetic converters*, you substitute any spoken words for simple thoughts, granting the subtle trait to the spell you're casting.

**Activate—Mental Fling** `pf2:2` (manipulate)

**Requirements** You have a spellcasting class feature and you can cast cantrips

**Effect** You cast [[Telekinetic Projectile]] as an occult cantrip, heightened to a spell rank equal to half your level rounded up.

**Activate—Mind Over Matter** `pf2:2` (manipulate)

**Requirements** You have a spellcasting class feature and have an unexpended spell slot of 5th rank or higher

**Effect** You cast your choice of [[Telekinetic Haul]] or [[Telekinetic Maneuver]] as a 5th-rank occult spell, consuming one of your unexpended spell slots of the same rank as if you had used it to cast the spell.

**Source:** `= this.source` (`= this.source-type`)
