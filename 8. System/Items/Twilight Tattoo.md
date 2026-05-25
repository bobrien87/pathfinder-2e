---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 125}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** You're a member of the Twilight Talons.

This tattoo of a black eagle gripping a sword and arrows in its talons identifies the bearer as a member of the Twilight Talons. Agents typically keep the tattoo hidden unless they need to prove their identity to another member. The bearer gains a +1 item bonus to Deception checks.

**Activate—Fade** `pf2:1` (concentrate, illusion)

**Effect** You hide your tattoo from view. The tattoo is invisible for 1 day and can't be detected by effects such as detect magic and read aura. You can Dismiss this effect.

**Activate—Inscribe** `pf2:2` (concentrate, illusion, manipulate)

**Frequency** once per day

**Effect** You lay your hand on a piece of text, and your tattoo makes a perfect copy of it, storing it as a ring of swirling letters surrounding the design. The tattoo can hold text equivalent to two pages of a book, a single scroll, or a similar area of other surfaces, though it doesn't replicate any magical effect or other special properties of the original words. You can Dismiss this effect, and when you Dismiss it, the tattoo copies the original text onto a blank writing surface you're touching.

**Source:** `= this.source` (`= this.source-type`)
