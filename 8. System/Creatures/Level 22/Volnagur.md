---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Volnagur"
level: "22"
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
    desc: "+39; [[Darkvision]]"
languages: "Aklo (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +42, Performance +45"
abilityMods: ["+9", "+11", "+11", "-2", "+3", "+7"]
abilities_top:
  - name: "Slumbering Armageddon"
    desc: "Volnagur's slumber increases the rate of wildlife attacks, swarms of vermin and pests, and violent crime. <br>  <br> Spawn of Rovagug can sleep for centuries in a regenerative hibernation. While slumbering, a Spawn doesn't need to eat, drink, or even breathe, and its resistances double in value. It can't be located by detection, revelation, or scrying effects, and for any saving throw, it uses the outcome one degree of success better than the result. With no outlet while the Spawn slumbers, its massive destructive energies turn outward and infect its surroundings, causing natural disasters of a type matching the Spawn to occur more frequently and with greater severity in a 1-mile emanation from the Spawn's resting place, increasing in radius by roughly a mile every decade the Spawn slumbers."
  - name: "Endsong"
    desc: "Subtle vibrations laced under Volnagur's attacks confuse its targets and fill their minds with the desire to destroy. A creature damaged by one of Volnagur's Strikes must attempt a DC 45 [[Will]] save. <br> - **Critical Success** The target is unaffected and is temporarily immune for 24 hours or until it takes damage from Scream of the End. <br> - **Success** The target is unaffected. <br> - **Failure** The target is [[Confused]] for 1d4 rounds. It never attempts to attack Volnagur or another creature affected by endsong. <br> - **Critical Failure** As failure, but the target is confused for 1 hour. While confused, its Strikes resonate with Volnagur's song, dealing an additional 1d6 sonic damage and forcing the target to save against endsong."
armorclass:
  - name: AC
    desc: "48; **Fort** +39, **Ref** +36, **Will** +33"
health:
  - name: HP
    desc: "515; absolute regeneration 25; **Immunities** clumsy, disease, drained, enfeebled, mental, paralyzed, petrified, poison, polymorph, sonic, stupefied"
abilities_mid:
  - name: "Absolute Regeneration"
    desc: "Volnagur's regeneration can be deactivated if a choir of no less than 12 exquisitely skilled and inspired individuals sings a song of beginnings and hope over its corpse for 1 year and 1 day without pause or flaw. <br>  <br> This functions as regeneration, though it requires very specific actions to be deactivated. A Spawn of Rovagug's regeneration is powerful enough to revive it even if slain by a death effect. If the Spawn fails a save against an effect that would kill it instantly, it rises from death 3 rounds later with 1 Hit Point. A Spawn can still be banished, imprisoned, or transported away as a means to save a region or kept in a state of dying by an effect that deals constant damage."
  - name: "Alien Harmonics"
    desc: "60 feet. <br>  <br> Volnagur constantly emits a cacophony that drowns out sound and thought while reinforcing Volnagur's song. Creatures that enter the aura must attempt a DC 43 [[Fortitude]] save or Volnagur's song becomes all they can hear for as long as they remain within the aura, making creatures [[Deafened]] against all sources other than Volnagur. <br>  <br> On a critical failure, the effect is permanent, and the cacophony rings in the target's ears regardless of range. The aura also attempts to counteract any auditory effect, any effect that would provide resistance or immunity to auditory or sonic effects, or any effect that would create silence (counteract rank 10, counteract modifier +33)."
  - name: "Frightful Presence"
    desc: "300 feet. DC 42 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Intercepting Eyes"
    desc: "`pf2:r` **Trigger** Volnagur is targeted by a ranged attack <br>  <br> **Requirements** Volnagur is aware of the attack and not [[Off Guard]] to it <br>  <br> **Effect** One of Volnagur's eyes fixes on the attack, shooting it down with an eye beam. The attack becomes a critical failure."
  - name: "Reactive"
    desc: "Volnagur gains 3 reactions each round. It can still use only one reaction per trigger."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +41 (`pf2:1`) (finesse, reach 20 ft.), **Damage** 4d10+24 piercing plus [[Endsong]] plus [[Grab]]"
  - name: "Melee strike"
    desc: "Razor Tongues +41 (`pf2:1`) (finesse, reach 40 ft.), **Damage** 4d8+24 slashing plus [[Endsong]] plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Eye Beam +41 (`pf2:1`) (magical, sonic, range 120 ft.), **Damage** 6d12 sonic plus [[Endsong]]"
spellcasting: []
abilities_bot:
  - name: "Gaze Upon"
    desc: "`pf2:2` Volnagur makes an eye beam Strike against every creature in a @Template[type:cone|distance:120]. These attacks count toward Volnagur's multiple attack penalty, but the multiple attack penalty doesn't increase until after Volnagur makes all its attacks. It can't use Gaze Upon again for 1d4 rounds, but until the start of Volnagur's next turn, it can use Intercepting Eyes as a free action."
  - name: "Scream of the End"
    desc: "`pf2:2` **Requirements** Volnagur has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** Volnagur holds a creature close to its eyes before blasting the creature at point-blank range. Volnagur deals 23d6 sonic damage to the target (DC 46 [[Reflex]] save). Regardless of the save's result, the target is no longer grabbed or restrained, is pushed 120 feet away from Volnagur, and falls [[Prone]]."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Of all Rovagug's spawn, the creature known as Volnagur is the one that has most distanced itself from the Dead Vault at Golarion's core, instead making its home among the skies. Volnagur possesses many wings, and they're mismatched, asymmetrical, and uncoordinated, yet the massive spawn is capable of powerful flight that carries it as far as Arcadia, Tian Xia, and even Sarusan. Though capable of wreaking great destruction with both its many razor-sharp tongues and powerful blasts of energy from its four eyes, Volnagur's most fearsome ability is the discordant song produced by the precise angling of its wings against the wind, which drives all who hear it to violence, setting neighbor against neighbor.

Though not spotted for decades, astronomers have recently located a satellite in the upper bounds of Golarion's atmosphere, where Volnagur hangs motionless. As it drifts from continent to continent, its eyes seem to alternately turn to the moon, then back to Golarion, as if waiting for a signal.

Though the destroyer god Rovagug lies trapped in the core of the planet like a fly trapped in amber, imprisoned since the Age of Creation by a coalition of deities, his cage has weakened with the passing of time, allowing his influence to seep forth and take form as living calamities known as the Spawn of Rovagug. These massive creatures have plagued Golarion for eons, their rampages responsible for shattered mountains, blasted deserts, and oceans that now fill craters in the earth, and their regenerative abilities ensure they're an eternal threat, never fully killed. That these creatures of utter destruction hold such a inextinguishable grip on life is a paradox scholars struggle to resolve. Some believe that each Spawn possesses the smallest fragment of their divine parent's blessings; others posit that their immortality comes from the destruction they cause, gaining an eternal future for every one stolen from their victims.

Accounts of the Spawns' attacks throughout history have an odd through line: each attack is followed by a notable, if brief, golden age for the region. While most attribute this to the cooperation required to fend off or at the very least survive a Spawn's depredations, some see this is a twisted sign that the creatures are bringers of "true" peace. These believers often lead cults intent on calling forth or reviving any recently slain Spawn.

Though many of the Spawn haven't been seen in years, the death of the god Gorum—one of the original architects of the Dead Vault—has weakened the seal once more, sending a ripple of Rovagug's will throughout Golarion. As if in answer, many of his Spawn have begun to reemerge, alarming Golarion's leaders, scholars, and warriors. After all, if a single Spawn is a generation-defining disaster, requiring the sacrifice of armies merely to minimize the damage it can cause, what unimaginable destruction would occur if all of them were to awaken at once?

```statblock
creature: "Volnagur"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
