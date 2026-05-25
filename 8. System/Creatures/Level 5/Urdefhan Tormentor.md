---
type: creature
group: ["Humanoid", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Urdefhan Tormentor"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Unholy"
trait_03: "Urdefhan"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Greater Darkvision]]"
languages: "Aklo, Daemonic, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +8, Crafting +9, Intimidation +11, Occultism +12, Religion +13"
abilityMods: ["+3", "+1", "+3", "+2", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +10, **Will** +15"
health:
  - name: HP
    desc: "75; **Immunities** death effects, disease, fear effects; **Weaknesses** vitality 5"
abilities_mid:
  - name: "Necrotic Decay"
    desc: "When an urdefhan dies, their translucent flesh quickly rots away and sublimates into a foul-smelling gas that fills a @Template[type:emanation|distance:5] around the body. This gas deals @Damage[5d6[void]|options:area-damage] damage to creatures in this area as their flesh curdles and rots (DC 21 [[Fortitude]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +12 (`pf2:1`) (shove), **Damage** 1d8+5 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`), **Damage** 2d6+5 piercing plus [[Wicked Bite]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15<br>**3rd** [[Paralyze]]<br>**2nd** [[Darkness]], [[False Vitality]], [[See the Unseen]]<br>**1st** [[Enfeeble]], [[Gentle Landing (Self Only)]], [[Grim Tendrils]], [[Harm]], [[Harm]], [[Harm]]"
abilities_bot:
  - name: "Stoke the Fervent"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The urdefhan lets out a battle cry, sending themself and their allies into a fanatical frenzy. The tormentor and each ally that hears the call gains a +1 status bonus to attack rolls, damage rolls, and saving throws, and takes a –1 status penalty to AC. Affected creatures must use at least one of their actions to Strike each round, if they're able (even if it means attacking an ally, object, or thin air). This lasts for 2d4 rounds."
  - name: "Wicked Bite"
    desc: "`pf2:1` **Requirements** The urdefhan damaged a creature with a jaws Strike on their last action <br>  <br> **Effect** The urdefhan maintains contact, turning the creature's flesh translucent around the site of the injury. The target must succeed at a DC 22 [[Fortitude]] save or be affected by drain blood or drain vitality (the urdefhan's choice). If the jaws Strike was a critical hit, the creature is affected by both effects, using the same save result for both. <br>  <br> - **Drain Blood** The urdefhan drinks some of the creature's blood. On a failed save, the creature is [[Drained]] 1 and the urdefhan regains 5 HP (or, on a critical failure, it's [[Drained]] 2 and the urdefhan regains 10 HP). <br> - **Drain Vitality** The urdefhan draws out some of the creature's vital essence. The creature becomes [[Enfeebled]] 1 for 1 hour on a failed save (or [[Enfeebled]] 2 for 1 hour on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Urdefhan spellcasters with a knack for the divine are invariably unholy worshippers of daemonkind, typically taking on one of Abaddon's Four Apocalypse Riders as their patron deity. With their unholy gifts, these urdefhan tormentors summon daemons into battle and bolster their allies with profane magic, preferring to stick to the sidelines rather than enter the fray directly.

The violent warmongers, occultists, and poisoners known as urdefhans dwell within the Darklands. They were created in eons past by the mysterious First Apocalypse Riders to serve as agents of the end times of the Universe. Urdefhans continue to honor their creators by worshipping the wretched beings who rule over the plane of Abaddon, and like their fiendish lieges, urdefhans exist for one reason and one reason alone: to kill.

While urdefhans are humanoid and dwell together in large groups, this is where their similarities to other ancestries end. Their visages are horrific, with transparent skin and musculature displaying their glistening entrails, gleaming bones, and perhaps worst of all, their baleful red eyes. This appearance, combined with their gaping maws full of sharp fangs, works to create the false impression that urdefhan are some sort of vampiric undead, not creatures of living flesh and blood. When an urdefhan's life comes to an end, their flesh quickly curdles and then bursts in a wave of awful corruption that spreads to the flesh of other creatures in the area. The typical urdefhan views their eventual demise as a disappointment, for once they're dead, their chances to kill will finally come to an end.

An urdefhan's translucent body allows onlookers to see the various organs and fluids within, while their blue blood often signals their mood and telegraphs possible dangers. The blood of an excited urdefhan ready to attack grows more vibrant and even glows with a faint light. When an urdefhan is prepared to meet their death and imminent soul detonation, their blood grows dark, almost black as pitch.

Urdefhans' primary concern is death and how to inflict it in the goriest, most painful, and widespread ways. Beyond this ethos of violence, urdefhans concern themselves only tangentially with matters such as formal modes of warfare or aspects of their damnable religion. When an urdefhan isn't actively engaged in violence, their giddy cruelty is tempered by only a sense of self-preservation that ensures they survive long enough to spread the "blessings" of their daemonic patrons. They pass the time between wars inventing new weapons, developing new diseases, and researching awful new magic, all in preparation for the next inevitable conflict.

```statblock
creature: "Urdefhan Tormentor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
