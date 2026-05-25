---
type: item
source-type: "Remaster"
level: "22"
traits: ["[[Artifact]]", "[[Cursed]]", "[[Illusion]]", "[[Invested]]", "[[Primal]]", "[[Shadow]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This palm-sized talisman hangs on a string of braided bark fibers. It resembles a leaf from some unknown tree similar to oak, carved from jade and then dipped halfway into black ink that looks wet despite feeling completely dry. The gate key was originally created to open the aiudara known as the Seventh Arch. In recent years, corrupting magic has given it additional, stranger powers.

When you wear and invest the *Shadewither Key*, shadows gather around you. You gain a +1 item bonus to Stealth checks.

**Activate** `pf2:2` Interact

**Activate—Umbral Double** `pf2:1` (concentrate, manipulate)

**Effect** You touch the *Shadewither Key* and command the shadows it casts around you to peel away. The shadows form an umbral double that resembles you in every way except for its fiery red eyes and the expression of wicked delight on its face. The double occupies the same space as you and attempts to intercept any attacks aimed at you. A creature must succeed at a DC 11 flat check when targeting you with an attack, spell, or other effect; on a failure, they hit the shadowy double instead of you. The effect lasts for 1 minute or until the double is hit, whichever comes first. Once the double is hit, it's destroyed. As long as the double exists, you don't gain the *Shadewither Key's* item bonus to Stealth checks.

**Source:** `= this.source` (`= this.source-type`)
