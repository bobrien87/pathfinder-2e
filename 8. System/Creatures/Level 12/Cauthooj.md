---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cauthooj"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Thoughtsense]] (imprecise) 60 feet"
languages: "Fey ((can't speak any language))"
skills:
  - name: Skills
    desc: "Athletics +24, Stealth +25"
abilityMods: ["+6", "+4", "+7", "-3", "+2", "+0"]
abilities_top:
  - name: "Thoughtsense (Imprecise) 60 feet"
    desc: "The cauthooj senses all non-mindless creatures at the listed range."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +20, **Will** +18"
health:
  - name: HP
    desc: "215; **Resistances** sonic 15"
abilities_mid:
  - name: "Hop-Dodge"
    desc: "`pf2:r` **Trigger** The cauthooj is the target of a melee Strike and is adjacent to another enemy that is also within the reach of the melee Strike. <br>  <br> **Effect** The cauthooj nimbly hops aside, redirecting the triggering Strike against the adjacent enemy. The cauthooj Strides up to half its Speed, and this movement does not trigger reactions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +26 (`pf2:1`) (agile, deadly d12, reach 10 ft., unarmed), **Damage** 2d12+12 piercing"
spellcasting: []
abilities_bot:
  - name: "Staccato Strike"
    desc: "`pf2:1` With subtle alterations in the pitch and tone of its song, the cauthooj directs one creature [[Confused]] by its Warbling Song to make a Strike. This works like other Strikes made by confused creatures, except that the cauthooj chooses the target. If no target is in reach or range, or the creature is unable to Strike for any other reason, this ability has no effect."
  - name: "Warbling Song"
    desc: "`pf2:2` The cauthooj gives a strange, ululating cry that causes nearby creatures to lash out violently and without control. Each creature within @Template[emanation|distance:120] that can hear the cauthooj must attempt a DC 32 [[Will]] save to resist the effect. <br> - **Critical Success** The target is unaffected and is temporarily immune for 1 minute. <br> - **Success** The target is unaffected. <br> - **Failure** The target is [[Confused]] for 1 round. <br> - **Critical Failure** The target is [[Confused]] for 1 round and immediately attacks itself (in the normal fashion for attacking oneself while confused). This Strike doesn't give the creature a flat check to recover from the confusion."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These large, flightless birds are deceptively agile, considering their long bodies and awkward, hopping gait. Solitary predators, they use their hypnotic warbling song to drive prey into a wild frenzy, manipulating them into attacking one another so that the cauthooj can then feast on the remains.

Known to some scholars as the puppet master bird, and to others as the shrill shrike, cauthoojs are widely reviled by most intelligent humanoids, in part because they seem to prefer humanoids as prey. Sightings typically lead to the creation of hunting parties to track the creature down before it can kill again, with would-be hunters typically stuffing their ears full of wax in an effort to avoid being affected by its cry. Those who have survived the creature's song report that the experience is uniquely unnerving, and almost all accounts agree that there is no other sound as terrible.

While one might assume the cauthooj is an unintelligent animal, these creatures are smarter than they look. Cauthoojs stalk the perimeter of remote settlements in hopes of finding a lone traveler they can feast upon. They can even understand a few rudimentary words in Fey, although they are incapable of clearly speaking themselves. This doesn't stop the cauthooj from attempting to mimic the sounds it hears, but when it does so, its eerie primal nature enhances the attempt, leading to the bird's signature ability to manipulate minds and encourage conflict, a trait the cauthooj is just barely smart enough to understand—and enjoy

```statblock
creature: "Cauthooj"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
