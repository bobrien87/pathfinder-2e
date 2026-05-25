---
type: deity
source-type: "Remaster"
domains: "Creation, Freedom, Knowledge, Metal"
favored-weapon: "Polytool"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Carryall]], Rank 3: [[Hypercognition]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Casandalee is an unusual god, one who achieved divinity through a merging of advanced science and faith. Formerly an artificial intelligence cloned from the mind of an android from outer space, Casandalee gained her godhood in the heart of Numeria within the computer core of a crashed spaceship, becoming the patron of artificial life, free thinking, and intellectual apotheosis.

Though she is sometimes referred to as the Iron Goddess, Casandalee is much more than simple metal. She sometimes appears as a holographic reconstruction of her android form: a female humanoid with purple hair, blue lips, and pale skin traced with glowing circuitry, but upon close inspection, this image seems to consist of millions of complex algorithms of pure light. Casandalee and her followers seek to promote the advancement of Golarion's technology so that the world's inhabitants can better understand- and not fear-the complex mechanisms of so-called artificial life, including androids and free-willed artificial intelligences. Many androids consider themselves the chosen people of Casandalee and depict her as an obvious android with more circuitry or exposed components.

**Title** The Iron Goddess

**Areas of Concern** artificial life, free thinking, intellectual apotheosis

**Edicts** advance the development of artificial intelligence, encourage understanding between artificial and organic life

**Anathema** treat artificial life as lesser than organic life, foment distrust between artificial and organic life

**Religious Symbol** gold etching on a blue chip

**Sacred Animal** moth

**Sacred Color** blue, gold

**Source:** `= this.source` (`= this.source-type`)
