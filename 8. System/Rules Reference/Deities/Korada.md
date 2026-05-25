---
type: deity
source-type: "Remaster"
domains: "Change, Healing, Magic, Protection"
favored-weapon: "Fist"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Soothe]], Rank 3: [[Slow]], Rank 4: [[Containment]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Korada, the Open Hand of Harmony, is concerned with foresight, forgiveness, and peace. In particular, he believes that although the tireless fight against wickedness is admirable, the ultimate triumph over evil will come in the form of redemption rather than destruction. Korada's dedication to peace is such that he and his followers refuse to cause harm to their attackers, instead using their martial skills only to defend themselves. Many Koradans seek greater wisdom through study or meditation in hopes of better understanding their foes so as to guide them toward redemption. This dedication to self-awareness, philosophy, and introspection is said to have allowed Korada greater insight into the workings of the universe, granting him the great gift of foresight. Korada rarely acts on his visions, however, believing the struggle that comes with true change is always worthwhile, whether or not such a change is successful.

**Title** The Open Hand of Harmony

**Areas of Concern** Foresight, forgiveness, peace

**Edicts** Forgive those who have wronged you, embrace a peaceful mindset, seek and allow redemption

**Anathema** Cause lethal harm to a creature, deny a repentant creature an opportunity for redemption, ask a retired warrior to fight

**Religious Symbol** lotus above two figures

**Sacred Animal** monkey

**Sacred Colors** green, purple

**Source:** `= this.source` (`= this.source-type`)
