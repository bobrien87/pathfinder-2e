---
type: creature
group: ["Earth", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lampad Queen"
level: "15"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]]"
languages: "Aklo, Common, Fey, Petran, Sakvroth (Speak with stones)"
skills:
  - name: Skills
    desc: "Acrobatics +27, Athletics +28, Deception +31, Diplomacy +33, Intimidation +33, Nature +27, Occultism +27, Performance +29, Society +25, Stealth +27"
abilityMods: ["+3", "+8", "+7", "+4", "+4", "+8"]
abilities_top:
  - name: "Cavern Empathy"
    desc: "The lampad queen can use Diplomacy to [[Make an Impression]] on and make very simple [[Requests]] of subterranean animals, plants, and fungi, as well as stones."
  - name: "Tied to the Land"
    desc: "A lampad queen is intrinsically tied to a specific underground region, usually a cave system. As long as the queen is healthy, the environment is exceptionally resilient, allowing the lampad queen to automatically attempt to counteract spells and rituals such as [[Blight]] that would harm the environment, with a +30 counteract modifier and a counteract rank of 8. <br>  <br> When the lampad queen becomes physically or psychologically unhealthy, however, her warded region eventually becomes twisted or unhealthy as well. In that case, restoring the lampad queen swiftly heals the entire region."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "38; **Fort** +26, **Ref** +29, **Will** +25"
health:
  - name: HP
    desc: "235; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Nymph's Beauty"
    desc: "30 feet. Creatures that start their turn in the aura must succeed at a DC 33 [[Will]] save or be [[Confused]] by the lampad queen's unearthly beauty for 1 minute. While confused by this effect, the creature's confused actions never include harming the lampad queen."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Earthen Fist +29 (`pf2:1`) (agile, finesse), **Damage** 3d10+9 bludgeoning plus 1d6 mental"
  - name: "Ranged strike"
    desc: "Light Wisp +29 (`pf2:1`) (magical, range 60 ft.), **Damage** 2d8+9 mental plus 2d6 fire plus 2d6 vitality"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 38, attack +30<br>**8th** (2 slots) [[Earthquake]], [[Summon Plant or Fungus]]<br>**7th** (3 slots) [[Energy Aegis]], [[Regenerate]], [[Volcanic Eruption]]<br>**6th** (3 slots) [[Petrify]], [[Slow]], [[Mountain Resilience]]<br>**5th** (3 slots) [[Impaling Spike]], [[Magic Passage]], [[Wall of Stone]]<br>**4th** (3 slots) [[Fly]], [[Unfettered Movement]], [[Resist Energy]]<br>**3rd** (3 slots) [[Earthbind]], [[Earthbind]], [[Haste]]<br>**2nd** (3 slots) [[Animal Messenger]], [[Enlarge]], [[Revealing Light]]<br>**1st** (3 slots) [[Ant Haul]], [[Fleet Step]], [[Gust of Wind]]<br>**Cantrips** [[Detect Magic]], [[Electric Arc]], [[Guidance]], [[Prestidigitation]], [[Stabilize]]"
  - name: "Primal Innate Spells"
    desc: "DC 38, attack +30<br>**4th** [[Shape Stone]]<br>**3rd** [[One with Stone]] (At Will)<br>**2nd** [[Revealing Light]]<br>**1st** [[Heal]], [[Light]], [[Pummeling Rubble]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` Lampad queens can transform between their original form, which looks much like a typical nymph of their kind, and any Small or Medium humanoid form, typically choosing a version of their natural form that more closely resembles a humanoid. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Despairing Weep"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The lampad queen begins a heart-wrenching fit of weeping, inspiring sympathetic sobbing in nearby creatures. Each non-lampad creature within @Template[emanation|distance:120]{120 feet} who hears the lampad's weeping must succeed at a DC 36 [[Will]] save with the effects of [[Wave of Despair]]."
  - name: "Focus Beauty"
    desc: "`pf2:1` The lampad queen focuses their beauty upon a target within their aura. The creature must attempt a DC 33 [[Will]] save. On a failure, it's affected as if by the queen's nymph beauty aura; if it was already affected by the aura, the conflicting emotions from the lampad queen's beauty intensify, causing the target to no longer get a flat check to end the confusion when it takes damage. The lampad queen can use a single action, which has the concentrate trait, to focus the emotions of a [[Confused]] creature toward a particular emotion, causing it to spend its next turn sobbing uncontrollably, fawning over the lampad queen, or otherwise performing no actions beyond experiencing its emotions. Regardless of the save, the target is temporarily immune to Focus Beauty until the start of the lampad queen's next turn."
  - name: "Inspiration"
    desc: "`pf2:3` A lampad queen can inspire a single intelligent creature by giving that creature a token of their favor, typically a lock of their hair. As long as the creature carries the token and remains in good standing with the lampad queen, the creature gains a +1 status bonus to all Crafting checks, Performance checks, and Will saves. <br>  <br> If a lampad queen grants their Inspiration to a bard and they're that bard's muse, the bard gains an additional benefit depending on their muse theme: for lore muse, the bard also gains a +1 status bonus to all Lore checks; for maestro muse, the status bonus to Performance checks increases to +2 for the purpose of determining the effects of compositions; for polymath muse, the bard gains a +4 status bonus to untrained skill checks; and for all other muses, the Will save bonus increases to +2 against fey. <br>  <br> > [!danger] Effect: Nymph Queen's Inspiration"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Lampad queens are capricious monarchs and protectors of vast underground domains, regarded in ballads and tales as allies and foes, monsters and muses. Lampad queens have a particular animosity for the many predominantly evil underground ancestries, such as drow and duergar, and they are particularly fond of bats. Many lampad queens have nykteras as favored attendants.

Nymphs are fey guardians of nature possessed of great beauty and forms that meld breathtaking humanoid features with the natural elements they guard. Nymph queens are powerful nymphs who rule over and protect a much greater territory of untouched wilderness. For instance, a lampad might guard a beautiful underground cavern, but a lampad queen might call an entire system of caves their domain.

```statblock
creature: "Lampad Queen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
