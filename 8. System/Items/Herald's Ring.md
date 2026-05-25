---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "worn"
bulk: "—"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Adorned with golden herald horns, this green ring both enhances a performer's vocal projection and provides partial protection against sonic attacks.

**Activate—Project Voice** `pf2:1` (manipulate)

**Frequency** Once per day

**Effect** When you turn the *herald's ring* around your finger three times in either direction, you gain the ability to easily project your voice up to 200 feet without raising the volume of speech, reaching your audience in most venues, including arenas. This effect lasts up to 2 hours.

**Activate—Reflect Sound** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You take sonic damage from a spell or effect

**Effect** You use the *herald's ring* to reflect a portion of the sonic damage back at its source by attempting to counteract the effect. The ring has a counteract modifier of +23.
- **Critical Success** All of the damage is reflected back on its source.
- **Success** Half of the damage is reflected back at its source, and the other half is negated.
- **Failure** Half of the damage is reflected back at the source, and you take the rest of the damage.
- **Critical Failure** None of the damage is reflected, but the herald's ring does absorb enough energy so that you can activate it again today.

**Source:** `= this.source` (`= this.source-type`)
