---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sacs full of dark ink have been implanted inside your mouth, allowing you to spit it forth.

**Activate—Spray Ink** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You splatter ink in a @Template[cone|distance:10], covering creatures and revealing [[Invisible]] ones. Each creature in the area must succeed at a DC 20 [[Reflex]] save or become covered in ink. If a creature has its invisibility negated by this ink, it is [[Concealed]] instead of invisible. A creature can negate the effects of the ink by spending two Interact actions to wipe off the ink.
- **Critical Success** The target is unaffected.
- **Success** The target's invisibility is negated for 2 rounds.
- **Failure** The target is [[Blinded]] for 1 round. Its invisibility is negated for 1 minute.
- **Critical Failure** The target is blinded for 10 minutes. Its invisibility is negated for 10 minutes.

If this graft is used underwater, you can instead choose to release the ink in a @Template[emanation|distance:10]. The resulting ink cloud lasts for 10 minutes. All creatures in the ink cloud become concealed, and all creatures outside the ink cloud become concealed to creatures within it.

**Source:** `= this.source` (`= this.source-type`)
