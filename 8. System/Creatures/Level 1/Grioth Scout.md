---
type: creature
group: ["Grioth", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grioth Scout"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Grioth"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Greater Darkvision]], [[Echolocation]] (precise) 20 feet"
languages: "Aklo, Grioth (telepathy 30 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Occultism +6, Stealth +7"
abilityMods: ["+0", "+4", "+2", "+1", "+2", "+0"]
abilities_top:
  - name: "Telepathy 30 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Echolocation (Precise) 20 feet"
    desc: "A grioth can use its hearing as a precise sense at the listed range."
  - name: "Grioth Venom"
    desc: "**Saving Throw** DC 17 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Frightened]] 1 (1 round) <br>  <br> **Stage 2** [[Frightened]] 2 (1 round) <br>  <br> **Stage 3** [[Frightened]] 3 (1 round)"
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "18; **Immunities** cold; **Weaknesses** fire 3"
abilities_mid:
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
  - name: "No Breath"
    desc: "A grioth doesn't breathe except to speak and is immune to effects that require breathing (such as an inhaled poison)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +7 (`pf2:1`) (agile, finesse, trip), **Damage** 1d6 slashing"
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d4 piercing plus [[Grioth Venom]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 16, attack +8<br>**1st** [[Daze]], [[Detect Magic]], [[Phantom Pain]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Shock Mind"
    desc: "`pf2:2` The grioth scout makes a Strike with a voidglass weapon. <br>  <br> If the Strike hits, it deals an additional 1d6 mental damage, and the target must succeed at a DC 17 [[Will]] save (this has the incapacitation trait) or become [[Confused]] for 1 round."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The first grioths encountered on a new world are scouts. Typically traveling the vastness of space via one-way portals from their home worlds, grioth scouts never expect to see their homes again, as grioth leadership ensures true devotion to the colonization effort by stranding them on new worlds.

Planets that drift out of orbit from their stars grow cold and lifeless as they float through the Dark Tapestry. Such dead worlds are coveted by the horrific creatures known as grioths, who endure the awful cold on these wandering worlds and convert them into planetary temples devoted to the dark gods of the Elder Mythos. From these bastions of frozen darkness, grioths seek out warm, living worlds to tear away from their respective suns through forbidden rituals, a process that often takes numerous generations.

A single cultist typically leads a grioth scouting party, and the group seeks out a disused or forgotten location on the fringe of rural settlements as their initial invasion point. Over several generations, a grioth settlement grows powerful and conquers the surrounding cultures, and eventually, powerful grioths descend from the stars to begin the next stage of planetary conquest.

Grioths speak a language composed of trills and clicks. While capable of speaking other languages, they do so in dry, raspy voices. As grioths have wings, wriggling tails, and four-eyed, bat-like visages, many cultures mistakenly associate them with the evil Outer Planes, but they very much belong to this reality.

```statblock
creature: "Grioth Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
