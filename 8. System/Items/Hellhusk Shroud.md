---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 230}"
usage: "worncloak"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hooded cloak is popular among those who must evade or surveil fiendish authorities. The grisly secrets behind this garment belies its innocuous appearance; its fabrics include threads woven from the hair, blood, and scales of various devils. When invested, a hellhusk shroud doesn't appear to radiate a magic aura to [[Detect Magic]] or similar spells unless the spells are 4th rank or higher. As long as you're wearing the cloak, you can read and speak Diabolic.

**Activate—Horned Husk** `pf2:1` (illusion, manipulate, olfactory, visual)

**Frequency** once per day

**Effect** The cloak wraps around you, becoming a second skin that suffuses you with Hell's corrosive brimstone. Your appearance becomes that of a nondescript low-level devil, and you gain a +1 status bonus to your Deception checks when you Lie to maintain your disguise. To creatures with scent, you also smell like a devil.

**Activate—Hellish Senses** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Effect** You pull your hood up, allowing the remnants of fallen devils to nestle closely and whisper Hell's secrets. You gain fiendsense as an imprecise sense within 60 feet, allowing you to sense creatures with the fiend trait as a vague sense. This effect lasts for 10 minutes or until you take this action again.

**Source:** `= this.source` (`= this.source-type`)
