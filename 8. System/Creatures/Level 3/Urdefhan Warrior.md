---
type: creature
group: ["Humanoid", "Urdefhan"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Urdefhan Warrior"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Urdefhan"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Greater Darkvision]]"
languages: "Aklo, Daemonic, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +10, Intimidation +9, Religion +7, Survival +7"
abilityMods: ["+3", "+1", "+2", "+0", "+2", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +8, **Will** +9"
health:
  - name: HP
    desc: "55; **Immunities** death effects, disease, fear effects; **Weaknesses** vitality 5"
abilities_mid:
  - name: "Necrotic Decay"
    desc: "When an urdefhan dies, their translucent flesh quickly rots away and sublimates into a foul-smelling gas that fills a @Template[type:emanation|distance:5] around the body. This gas deals @Damage[3d6[void]|options:area-damage] damage to creatures in this area as their flesh curdles and rots (DC 17 [[Fortitude]] save)."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rhoka Sword +12 (`pf2:1`) (deadly d8, two hand d10), **Damage** 1d8+6 slashing"
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`), **Damage** 1d6+6 piercing plus [[Wicked Bite]]"
  - name: "Ranged strike"
    desc: "Composite Longbow +10 (`pf2:1`) (deadly d10, propulsive, volley 30, range 100 ft.), **Damage** 1d8+4 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Darkness]]<br>**1st** [[Enfeeble]], [[Gentle Landing (At Will, Self Only)]]"
abilities_bot:
  - name: "Ravenous Attack"
    desc: "`pf2:2` The urdefhan makes one rhoka sword Strike and one jaws Strike against a single creature. Their multiple attack penalty doesn't increase until after both attacks."
  - name: "Wicked Bite"
    desc: "`pf2:1` **Requirements** The urdefhan damaged a creature with a jaws Strike on their last action <br>  <br> **Effect** The urdefhan maintains contact, turning the creature's flesh translucent around the site of the injury. The target must succeed at a DC 20 [[Fortitude]] save or be affected by drain blood or drain vitality (the urdefhan's choice). If the jaws Strike was a critical hit, the creature is affected by both effects, using the same save result for both. <br>  <br> - **Drain Blood** The urdefhan drinks some of the creature's blood. On a failed save, the creature is [[Drained]] 1 and the urdefhan regains 5 HP (or, on a critical failure, it's [[Drained]] 2 and the urdefhan regains 10 HP). <br> - **Drain Vitality** The urdefhan draws out some of the creature's vital essence. The creature becomes [[Enfeebled]] 1 for 1 hour on a failed save (or [[Enfeebled]] 2 for 1 hour on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

From the moment they're born, urdefhans are prepared for war. Urdefhan warriors are among the least powerful urdefhans one might encounter outside of their eerie underground cities.

The violent warmongers, occultists, and poisoners known as urdefhans dwell within the Darklands. They were created in eons past by the mysterious First Apocalypse Riders to serve as agents of the end times of the Universe. Urdefhans continue to honor their creators by worshipping the wretched beings who rule over the plane of Abaddon, and like their fiendish lieges, urdefhans exist for one reason and one reason alone: to kill.

While urdefhans are humanoid and dwell together in large groups, this is where their similarities to other ancestries end. Their visages are horrific, with transparent skin and musculature displaying their glistening entrails, gleaming bones, and perhaps worst of all, their baleful red eyes. This appearance, combined with their gaping maws full of sharp fangs, works to create the false impression that urdefhan are some sort of vampiric undead, not creatures of living flesh and blood. When an urdefhan's life comes to an end, their flesh quickly curdles and then bursts in a wave of awful corruption that spreads to the flesh of other creatures in the area. The typical urdefhan views their eventual demise as a disappointment, for once they're dead, their chances to kill will finally come to an end.

An urdefhan's translucent body allows onlookers to see the various organs and fluids within, while their blue blood often signals their mood and telegraphs possible dangers. The blood of an excited urdefhan ready to attack grows more vibrant and even glows with a faint light. When an urdefhan is prepared to meet their death and imminent soul detonation, their blood grows dark, almost black as pitch.

Urdefhans' primary concern is death and how to inflict it in the goriest, most painful, and widespread ways. Beyond this ethos of violence, urdefhans concern themselves only tangentially with matters such as formal modes of warfare or aspects of their damnable religion. When an urdefhan isn't actively engaged in violence, their giddy cruelty is tempered by only a sense of self-preservation that ensures they survive long enough to spread the "blessings" of their daemonic patrons. They pass the time between wars inventing new weapons, developing new diseases, and researching awful new magic, all in preparation for the next inevitable conflict.

```statblock
creature: "Urdefhan Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
