---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sorvuth-Ka"
level: "24"
rare_01: "Unique"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+42; [[Darkvision]]"
languages: "Aklo (can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +45, Athletics +45, Intimidation +41, Survival +45"
abilityMods: ["+12", "+9", "+12", "+10", "+7", "+5"]
abilities_top:
  - name: "Slumbering Armageddon"
    desc: "Sorvuth-ka's slumber accelerates erosion and weathering, timed to always break at the point of maximum harm via rockslides, sinkholes, treefalls, and other collapses. <br>  <br> Spawn of Rovagug can sleep for centuries in a regenerative hibernation. While slumbering, a Spawn doesn't need to eat, drink, or even breathe, and its resistances double in value. It can't be located by detection, revelation, or scrying effects, and for any saving throw, it uses the outcome one degree of success better than the result. With no outlet while the Spawn slumbers, its massive destructive energies turn outward and infect its surroundings, causing natural disasters of a type matching the Spawn to occur more frequently and with greater severity in a 1-mile emanation from the Spawn's resting place, increasing in radius by roughly a mile every decade the Spawn slumbers."
armorclass:
  - name: AC
    desc: "52; **Fort** +42, **Ref** +38, **Will** +36"
health:
  - name: HP
    desc: "550; absolute regneration 25; **Immunities** clumsy, disease, drained, enfeebled, mental, paralyzed, petrified, poison, polymorph, stupefied, visual"
abilities_mid:
  - name: "Absolute Regeneration"
    desc: "Sorvuth-ka's regeneration can be deactivated by slaying it with a weapon made from the bones of Chemnosit, Kothogaz, Ulunat, Volnagur, and Xotani. <br>  <br> This functions as regeneration, though it requires very specific actions to be deactivated. A Spawn of Rovagug's regeneration is powerful enough to revive it even if slain by a death effect. If the Spawn fails a save against an effect that would kill it instantly, it rises from death 3 rounds later with 1 Hit Point. A Spawn can still be banished, imprisoned, or transported away as a means to save a region or kept in a state of dying by an effect that deals constant damage."
  - name: "Adaptive Defenses"
    desc: "When injured, Sorvuth-ka's body adapts to ensure that the triggering insult can't harm it again. Immediately after it takes damage, it becomes immune to that type of damage. It can become immune to three different types of damage in this way, with newer immunities replacing older ones."
  - name: "Bleed Destruction"
    desc: "`pf2:0` **Trigger** Sorvuth-ka takes physical damage <br>  <br> **Effect** Amber blood spurts from Sorvuth-ka's wound, creating a blood pool in a square adjacent to Sorvuth-ka. The blood remains in the area until removed or it dries, which typically takes 1 day."
  - name: "Frightful Presence"
    desc: "300 feet. DC 45 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive"
    desc: "Sorvuth-ka gains 3 reactions each round. It can still use only one reaction per trigger."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +44 (`pf2:1`) (agile, finesse, reach 15 ft.), **Damage** 4d8+27 slashing plus [[Improved Grab]]"
  - name: "Ranged strike"
    desc: "Crystallized Blood +44 (`pf2:1`) (propulsive, range 120 ft.), **Damage** 5d6+21 slashing"
spellcasting: []
abilities_bot:
  - name: "Amber Strikes"
    desc: "`pf2:1` **Requirements** Sorvuth-ka's previous action was a successful Strike against the target <br>  <br> **Effect** After landing a Strike, Sorvuth-ka commands it blood to continue the assault, choosing one of the three following options: Crystallize, Inject, or Splash. If the previous attack was a critical hit, Amber Strikes is a free action. <br>  <br> - *Crystallize* Sorvuth-ka's blood flows around the target's limbs before hardening. The creature must succeed at a DC 48 [[Reflex]] save or become [[Immobilized]] and [[Off Guard]] until it Escapes. If the creature was flying, it falls. <br> - *Inject* Sorvuth-ka's blood invades the target through its wounds. The target must succeed at a DC 48 [[Fortitude]] save or become [[Sickened]] 2 ([[Sickened]] 3 on a critical failure). As long as the target is sickened, Sorvuth-ka's blood will attempt to counteract any effect that could restore Hit Points to the target (counteract rank 10, counteract modifier +38). <br> - *Splash* Sorvuth-ka's blood splashes violently, dazzling the target until the end of its next turn and creating a blood pool in a square adjacent to the target."
  - name: "Detonate Blood"
    desc: "`pf2:2` **Requirements** A pool of Sorvuth-ka's blood is within 500 feet <br>  <br> **Effect** Sorvuth-ka's blood detonates into crystalline amber flechettes. Every creature either in the required blood pool's square or in a @Template[type:emanation|distance:10] of that pool other than Sorvuth-ka takes @Damage[20d8[piercing]|options:area-damage] damage (DC 48 [[Reflex]] save). On a critical failure, any resistances to physical damage the creature has are reduced by 10 for 1 minute."
  - name: "Rough Rampage"
    desc: "`pf2:1` **Requirements** Sorvuth-ka has at least one creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** Sorvuth-ka Strides, dragging any creatures it's grabbed or restrained along with it. Each grabbed or restrained creature takes 11d6 bludgeoning damage (DC 48 [[Fortitude]] save). On a failure, the creature is also [[Clumsy]] 2 (or [[Clumsy]] 3 on a critical failure) until it Escapes."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sorvuth-ka is the youngest of Rovagug's spawn. It has never been seen eating; lacking the ravenous hunger observed in the other Spawn, it seems to destroy simply for the pleasure of it, approaching each of its attacks with novel, inventive cruelty. Sorvuth-ka might pause while destroying a town to give the populace just enough time to flee, only for them to realize in despair that their only route of escape is a mountain pass that Sorvuth-ka has already collapsed. However, the creature grows bored easily, swiftly dispatching prey with bladed limbs if its games stop going to plan or take too long to come to fruition.

Curiously, despite Sorvuth-ka's regenerative abilities—powerful even for a Spawn and capable of rendering it resistant to attacks that have injured it—it has several wounds that refuse to heal, most notably a great gash across its face. Some scholars theorize that these wounds are some cruel design of Rovagug, the better to allow access to the amber blood that is Sorvuth-ka's primary instrument of destruction. Others take it as proof of the existence of a weapon capable of ending the threat of the Spawn of Rovagug once and for all.

Though the destroyer god Rovagug lies trapped in the core of the planet like a fly trapped in amber, imprisoned since the Age of Creation by a coalition of deities, his cage has weakened with the passing of time, allowing his influence to seep forth and take form as living calamities known as the Spawn of Rovagug. These massive creatures have plagued Golarion for eons, their rampages responsible for shattered mountains, blasted deserts, and oceans that now fill craters in the earth, and their regenerative abilities ensure they're an eternal threat, never fully killed. That these creatures of utter destruction hold such a inextinguishable grip on life is a paradox scholars struggle to resolve. Some believe that each Spawn possesses the smallest fragment of their divine parent's blessings; others posit that their immortality comes from the destruction they cause, gaining an eternal future for every one stolen from their victims.

Accounts of the Spawns' attacks throughout history have an odd through line: each attack is followed by a notable, if brief, golden age for the region. While most attribute this to the cooperation required to fend off or at the very least survive a Spawn's depredations, some see this is a twisted sign that the creatures are bringers of "true" peace. These believers often lead cults intent on calling forth or reviving any recently slain Spawn.

Though many of the Spawn haven't been seen in years, the death of the god Gorum—one of the original architects of the Dead Vault—has weakened the seal once more, sending a ripple of Rovagug's will throughout Golarion. As if in answer, many of his Spawn have begun to reemerge, alarming Golarion's leaders, scholars, and warriors. After all, if a single Spawn is a generation-defining disaster, requiring the sacrifice of armies merely to minimize the damage it can cause, what unimaginable destruction would occur if all of them were to awaken at once?

```statblock
creature: "Sorvuth-Ka"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
