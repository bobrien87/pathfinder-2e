---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 2700}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved in this wooden disc is a humanoid eye, painted in muted shades that blend in with the wood. The eye's pupil continually twitches and moves, scanning its bearer's surroundings.

- **Armor** (revelation) You aren't [[Off Guard]] to [[Hidden]] or [[Undetected]] creatures of the eye's level or lower, or creatures of the eye's level or lower using surprise attack, though you can still be flanked.
- **Weapon** When you make a Strike with the weapon against a target that's [[Concealed]], hidden, or undetected, the DC of your flat check to target it is 2 if the target is concealed or 8 if it's hidden or undetected.

**Activate** Cast a Spell

**Effect** You cast [[Detect Magic]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Clairvoyance]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Scouting Eye]].

**Source:** `= this.source` (`= this.source-type`)
