---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jah-Tohl"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]], [[Thoughtsense]] (precise) 60 feet"
languages: "Aklo, Chthonian, Draconic, Protean, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +17, Arcana +18, Athletics +16, Occultism +21, Stealth +17, Lore (all subcategories) +18"
abilityMods: ["+6", "+3", "+5", "+4", "+4", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Thoughtsense 60 feet"
    desc: "The jah-tohl senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
  - name: "Mind Snatcher Venom"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d6 poison, enfeebled 1, and [[Slowed]] 1 (1 round) <br>  <br> **Stage 3** 2d6 poison, [[Enfeebled]] 2, and slowed 1 (1 round)"
armorclass:
  - name: AC
    desc: "26; **Fort** +15, **Ref** +13, **Will** +18"
health:
  - name: HP
    desc: "140; **Immunities** confused"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Brain Blisters"
    desc: "A jah-tohl has seven brain blisters on its back that it uses to house stolen brains. A jah-tohl without all seven blisters full is [[Stupefied]] with a value equal to the number of empty blisters."
  - name: "Brain Loss"
    desc: "If a jah-tohl takes 30 damage from a critical hit or 25 mental damage, it must succeed at a DC 26 save (DC 26 [[Fortitude]] save{Fortitude} for critical damage or DC 26 [[Will]] save{Will} for mental damage) or one of its brain blisters is destroyed."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (unarmed), **Damage** 2d12+6 piercing plus [[Brain Collector Venom]]"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, unarmed), **Damage** 2d8+6 slashing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18<br>**4th** (2 slots) [[Confusion]], [[Vision of Death]]<br>**3rd** (3 slots) [[Haste]], [[Paralyze]]<br>**2nd** (4 slots) [[Dispel Magic]], [[Humanoid Form]], [[Invisibility]], [[Paranoia]]<br>**1st** (4 slots) [[Detect Magic]], [[Enfeeble]], [[Figment]], [[Light]], [[Mindlink]], [[Sure Strike]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Collect Brain"
    desc: "`pf2:1` The jah-tohl extracts the brain of a creature within its reach that has been dead for no more than 1 minute. It can then use an Interact action to secure the brain in one of its empty brain blisters and heal 20 healing Hit Points."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The grotesque jah-tohl arrive in living starships to harvest the brains of intelligent creatures. These aberrations draw no nutrition from brains, instead storing them for analysis and as vessels for occult energies.

A mind snatcher's form evokes that of a tailless scorpion, but the pulsing brain-filled blisters that glisten along its back make them impossible to mistake for oversized arachnids. Baleful eyes glare from the joints on their legs, and the unsettling, intrusive whisper-thoughts they telepathically broadcast into the minds of those they seek to feed on can be interpreted as threats or promises alike.

Mind snatchers have little empathy for the denizens of any world they visit, despite the fact that certain cults venerate them and the Dominion they hail from. To mind snatchers, terrestrial creatures are simply resources for their investigations. They have little interest in gods or being worshipped, instead practicing a philosophy that considers the primordial forces of deep space as worthy of faith and fear. Jah-tohlian philosophers contemplate these mysterious forces from many perspectives at once, burning through numerous brains in the search of insight.

The Dominion of the Black is a conglomeration of deep-space conquerors with a strong presence on Aucturn, the most remote planet in Golarion's solar system. The Dominion has secret outposts all over Golarion; most of its members on the planet are scouts, using their skills to steal brains and identities, gathering information without any consideration for the inhabitants of the worlds they infiltrate.

```statblock
creature: "Jah-Tohl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
