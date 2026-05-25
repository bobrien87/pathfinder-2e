---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 950}"
usage: "worncollar"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elaborate choker is fashioned from the treated hide of a water orm. Its interior is lined with the creature's silky hair. While wearing an *orm choker*, your form blurs slightly around the edges, granting you a +1 item bonus to saving throws against detection, revelation, and scrying effects.

**Activate—Watery Form** `pf2:3` (concentration, water)

**Frequency** once per day

**Effect** You dissolve into liquid, appearing only as a stretch of flowing water. While in this form, you gain a swim Speed of 45 feet, you automatically succeed at Athletics checks to Swim, and you gain a +4 circumstance bonus to Stealth checks in water. However, you can't speak, use any of your other items or abilities, or enter a body of salt water while in this form. You can remain in this form for up to 1 hour, though you can return to your normal form using a single action that has the concentrate trait.

> [!danger] Effect: Watery Form

**Craft Requirements** The initial raw materials must include the hide and hair of a water orm.

**Source:** `= this.source` (`= this.source-type`)
