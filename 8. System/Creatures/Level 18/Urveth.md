---
type: creature
group: ["Darvakka", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Urveth"
level: "18"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Greater Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Common, Diabolic, Necril (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +29, Athletics +35, Religion +32, Stealth +31, Netherworld Lore +31, Void Lore +31"
abilityMods: ["+10", "+5", "+8", "+5", "+6", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Urveth Venom"
    desc: "**Saving Throw** DC 37 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** @Damage[3d6[void],2d6[poison]]{3d6 void damage and 2d6 poison damage} (1 round) <br>  <br> **Stage 2** @Damage[3d6[void],2d6[poison]]{3d6 void damage and 2d6 poison damage}, and [[Enfeebled]] 2 (1 round) <br>  <br> **Stage 3** @Damage[3d6[void],2d6[poison]]{3d6 void damage and 2d6 poison damage}, and [[Enfeebled]] 4 (1 round)"
armorclass:
  - name: AC
    desc: "40; **Fort** +32, **Ref** +29, **Will** +34"
health:
  - name: HP
    desc: "460; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** holy 15, silver 15; **Resistances** cold 15"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "60 feet. Urveths leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 5d6 void damage with a DC 38 [[Fortitude]] save. If it fails, it's also [[Enfeebled]] 1 for 1 minute and pulled 10 feet toward the urveth."
  - name: "Reactive Strike"
    desc: "`pf2:r` Claw only. An urveth gains 3 extra reactions each round that they can use only to make Reactive Strikes. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Sunlight Powerlessness"
    desc: "A urveth caught in sunlight is [[Stunned]] 2 and [[Clumsy]] 2."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +36 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 3d10+14 slashing plus 2d10 cold plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Claw +36 (`pf2:1`) (agile, magical, reach 15 ft., unarmed), **Damage** 3d6+14 slashing plus 2d10 cold"
  - name: "Melee strike"
    desc: "Stinger +36 (`pf2:1`) (magical, poison, reach 20 ft.), **Damage** 3d6+14 piercing plus 2d10 cold plus [[Urveth Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32<br>**7th** [[Eclipse Burst]], [[Interplanar Teleport (to the Universe, Void, or Netherworld only)]]<br>**6th** [[Truesight]]<br>**4th** [[Fly]] (Constant)<br>**2nd** [[Darkness]] (At Will)<br>**1st** [[Detect Magic]], [[Harm]]"
abilities_bot:
  - name: "Frenzy"
    desc: "`pf2:2` The urveth makes two claw Strikes and one stinger Strike in any order."
  - name: "Swallow Whole"
    desc: "`pf2:1` Huge, @Damage[(2d10+5)[bludgeoning]], Rupture 35 <br>  <br> A living creature that ends its turn swallowed whole by an urveth becomes [[Drained]] 1 or increases its drained condition by 1, and the urveth gains 10 temporary Hit Points. A creature whose drained condition increases to 5 in this way dies. <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An urveth is a massive, four-armed burrowing terror with a wormlike body and gaping maw that devours everything it can. Urveths burrow deep underground to hide from the sun, emerging under the cover of darkness to kill and consume.

Darvakkas, also called nightshades, are a ravenous evil made up of equal parts darkness and malice. Originally creatures of the Outer Planes who travel to the convergence of the Shadow Plane and the Void—where the power of nothingness obliterates them—these undead abominations are the physical embodiment of entropy. They burn with an intense hatred for all life, working to bring a final, dark night to the Material Plane where nothing but ash and ice remain.

As creatures twisted by darkness and shadow, darvakkas have a great aversion to sunlight and all sources of vitality energy. On the Material Plane, they spend the hours of daylight hidden below ground, amid ruins, or submerged deep in the ocean's darkest chasms beyond the reach of the sun's rays, emerging when darkness shelters them overhead.

Darvakkas have an aura of entropy that attracts undead thralls to serve as warriors and heralds. They rarely seek alliances with each other or other creatures, existing in solitude as the heads of individual armies of the dead.

```statblock
creature: "Urveth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
