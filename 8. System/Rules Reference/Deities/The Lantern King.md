---
type: deity
source-type: "Remaster"
domains: "Change, Passion, Trickery, Delirium"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 2: [[Laughing Fit]], Rank 6: [[Cursed Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Although the Lantern King most often appears as a floating ball of light surrounded by runes that form a delicate crown, the Eldest of laughter, mischief, and transformation has taken on a dizzying array of figures. He often adopts alternate shapes to play pranks, and even other Eldest are not immune to his mischievous scheming. Although he insists his pranks are intended only for levity and to bring down imperious snobs, the chaos he creates in the name of good-natured fun is, to his targets, embarrassing at best and sometimes outright lethal. The Lantern King wanders the First World more than other Eldest, and he can be encountered in crowded markets and lonely byways alike. He is frequently accompanied by the Witchmarket, a traveling caravan of entertainers and merchants that serves as his court.

**Title** The Laughing Lie

**Areas of Concern** Laughter, mischief, transformation

**Edicts** Play pranks, seek new jokes, leave lit lanterns in unusual places

**Anathema** Be completely honest, ruin or explain a good joke

**Religious Symbol** golden lantern

**Sacred Animal** firefly

**Sacred Colors** black, gold

**Source:** `= this.source` (`= this.source-type`)
