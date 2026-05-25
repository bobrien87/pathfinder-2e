---
type: item
source-type: "Remaster"
level: "25"
traits: ["[[Artifact]]", "[[Divine]]", "[[Magical]]", "[[Unholy]]", "[[Versatile p]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The weapon wielded in battle by Szuriel, Rider of War, is a perpetually blood-covered blade that has taken more lives than even the gods can count. *Lamentation of the Faithless* is a *+4 major striking quickstrike unholy greatsword* with a blade of unyielding jet-black steel that absorbs all incident light, counteracting all light effects in a 15-foot radius with a +37 modifier as long as the weapon is unsheathed. Any creature within range attempting to use a spell or ability with the light trait must first succeed at a DC 15 flat check, or the attempt fails. Whenever the blade strikes and deals damage to a living creature, its wielder regains 1d12 healing Hit Points.

**Activate—Lo and Behold** `pf2:1` (manipulate, unholy, visual)

**Frequency** once per day

**Effect** You raise Lamentation of the Faithless high above the battlefield, presenting its terrible glory for all to witness. All creatures within 60 feet that are able to see the sword must attempt a DC 50 [[Will]] save. Creatures with the unholy trait are immune to this effect, but creatures with the holy trait take a –2 status penalty on this save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is stricken by crushing despair. It becomes [[Slowed]] 1 as it sobs uncontrollably, and it can't use reactions while it's slowed.
- **Failure** As success, but the creature is also [[Blinded]] for 1 round.
- **Critical Failure** As failure, but the duration of the blinded condition is 1 minute.

**Destruction** *Lamentation of the Faithless* can only be destroyed if it's driven into the ground within the walls of the secluded garden at the summit of Heaven's mountain by a risen, repentant fiend, whereupon it shatters and crumbles to dust.

**Source:** `= this.source` (`= this.source-type`)
