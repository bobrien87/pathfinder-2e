---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
usage: "worn"
bulk: "L"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A miniaturization module is a bulky clockwork belt interwoven with clear rubber tubing. These tubes are filled with distilled liquid magic, which serves as a power source. While wearing a miniaturization module, you gain a +1 item bonus to checks to [[Escape]].

**Activate—Miniaturize Me!** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You instantly shrink, becoming Tiny in size. Your equipment shrinks with you but returns to its original size if removed. While Tiny, your reach changes to 0 feet. You remain Tiny for 10 minutes, but you can Dismiss this effect.

**Activate—Miraculous Escape** `pf2:r`

**Frequency** once per hour

**Trigger** You become [[Grabbed]], [[Immobilized]], or [[Restrained]]

**Effect** You instinctively trigger the miniaturization module and wiggle free, then move and grow larger, seemingly escaping in a flicker of motion. You become Tiny, then attempt to Escape the triggering effect, gaining a +4 circumstance bonus to this check. If you successfully Escape, you Step into an adjacent space. Regardless of the result, you then return to your original size.

**Source:** `= this.source` (`= this.source-type`)
