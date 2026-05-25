---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 1100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This crystal phial was created from Brilliance, a condensed planar fragment of the plane of Nirvana which is trapped within Gloaming Arbor. A *paradise light* glows brightly, shedding bright light in a 30-foot radius and dim light to a further 30 feet. A PC that looks into the *paradise light* sees images of Nirvana, an idyllic pastoral paradise. A *paradise light* is required to navigate the heart of the forest in Gloaming Arbor.

A *paradise light* automatically attempts to counteract any magical darkness that it's light enters. When the *paradise light* successfully counteracts an area of magical darkness, that area becomes overlain by a reflection of Nirvana, changing the appearance of the area. This illusory transformation lasts for 1 hour.

**Activate—Sanctum** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You conjure a shard of Nirvana in a 30 foot emanation, temporarily altering the landscape into an soothing meadow for 1 minute. Creatures in the area gain a +1 item bonus to Will saves and Wisdom-based skill checks, and have fast healing 2. A creature in the area that attempts to take a hostile action must succeed at a DC 28 [[Will]] save or the hostile action is prevented and the actions they would've spent are wasted.

**Source:** `= this.source` (`= this.source-type`)
