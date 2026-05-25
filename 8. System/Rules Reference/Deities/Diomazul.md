---
type: deity
source-type: "Remaster"
domains: "Destruction, Earth, Water, Zeal"
favored-weapon: "Scimitar"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Slough Skin]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

An obscure Vudran god of war, Diomazul, the Serpent of Eighty Blades, is a patron of ascetic meditation, bitter renewals, and inordinate retribution. Devotees and theologians speak of Diomazul as having the likeness of a massive, hooded cobra in serene slumber—80 arms folded in stillness comprise this hood, each hand grasping a sheathed blade. When roused to violence by enemies, Diomazul awakens, retaining his tranquil countenance, but his hood flares in a bristle of steel as he draws all 80 blades to welcome his newfound foes and offer a gift of their unmaking. Once the Serpent of Eighty Blades has concluded evicting the life from his enemies, he entwines his body around their remains, crushing their bones into the earth and scattering their blood into the waters, burying all spoor of their existence under his immense form.

As these depictions might suggest, Diomazul is a deity of dualistic, seemingly contradictory impulses who unifies the dichotomies of restraint and devastation within his being. Diomazul is a teacher of forbearance and detached contemplation, a paragon of indifference to personal contentment or suffering who meditates upon the universe, sloughing off whatever pain it can visit upon oneself. At the same time, Diomazul also embodies an endless, pitiless resolve to visit frightful destruction upon those who set themselves in opposition to him; once stirred from his reverie by insult or injury, vast and swift reprisal are sure to follow.

In many ways, the Serpent of Eighty Blades is exactly like his name suggests, a coiled being of muscle and killing intent in absolute control of razor-sharp steel. Diomazul's blades split time into two unequal halves for his enemies: the impermanence of existence before meeting him and the decidedly much shorter impermanence of existence after raising his ire.

**Title** The Serpent of Eighty Blades

**Areas of Concern** Austerity, retribution, war

**Edicts** Erase all traces of defeated foes, meditate, remain celibate and detached from worldly pleasures, utterly destroy your enemies

**Anathema** Give mercy to any who provoke a fight with you, provoke a fight

**Religious Symbol** cobra hood

**Sacred Animal** cobra

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
