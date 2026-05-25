---
type: deity
source-type: "Remaster"
domains: "Duty, Fire, Protection, Vigil"
favored-weapon: "Longspear"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Thunderstrike]], Rank 3: [[Phantom Prison]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Not seen outside their bastille of hellfire-stoked iron since their designation as a duke, Haborym keeps vigil over the most dangerous beings in the planes. Haborym's 8-milelong prison is a testament to their dedication, a crucible for the souls to be reforged anew. Any interned within have the option to challenge the governor to a single game of their choosing: early discharge for victory, servitude for defeat. To Haborym's dismay, not one prisoner has exercised this right in generations. Depictions show the Burning Hearth as a four-armed humanoid lacking a mouth and with skin that appears to have been burned to near ashes.

Those who serve their sentence all have volunteered to join the Panopticon's watch, guarding over their former fellow inmates. Lawkeeps who catch, judges who charge, and smiths who forge the bonds of captivity, who believe through continual breaking and reforging the weak are honed strong and true, these are the ilk of Haborym. "It is for their own good" is their guiding axiom.

**Title** The Burning Heath

**Areas of Concern** Immolation, incarceration, renewal

**Edicts** Identify all exits, take your enemies alive, enact malicious compliance

**Anathema** Deny clemency without offering an opportunity for appeal, wear chains or bracelets on your person, misplace anything within your charge

**Religious Symbol** burning spider web

**Sacred Animal** spider

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
