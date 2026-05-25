---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ostiarius"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Greater Darkvision]]"
languages: "Common, Diabolic, Shadowtongue (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Deception +12, Diplomacy +12, Intimidation +16, Religion +11, Torture Lore +11"
abilityMods: ["+0", "+4", "+2", "+2", "+4", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
  - name: "Sense Portal"
    desc: "The ostiarius always knows the direction and distance to the closest portal between the Netherworld and the Universe. This sense functions only on these two planes."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +15, **Will** +13"
health:
  - name: HP
    desc: "65; **Immunities** cold; **Weaknesses** holy 5, silver 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 5 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Whispering Wounds"
    desc: "30 feet. When a creature ends its turn in the aura, it hears the wounds on the ostiarius's body whisper obscene truths. The creature must succeed at a DC 21 [[Will]] save or become [[Sickened]] 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, finesse, magical, unholy), **Damage** 2d6 bleed plus 2d6+2 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16<br>**3rd** [[Enthrall]], [[Safe Passage]]<br>**2nd** [[Calm]] (At Will), [[Darkness]], [[Silence]]<br>**1st** [[Shield]]"
abilities_bot:
  - name: "Compel Courage"
    desc: "`pf2:1` The ostiarius inspires their willing allies and themself by whispering words of courage from their wounds. The ostiarius and their allies in a @Template[type:emanation|distance:50] gain a +1 status bonus to attack rolls, damage rolls, and saves against fear effects. The ostiarius can Sustain Compel Courage. Non-velstracs who accept this compelled courage find bleeding wounds opening on their own bodies to whisper in thanks. They take 1 bleed damage and can't attempt a flat check to end this damage as long as they're compelled. <br>  <br> > [!danger] Effect: Compel Courage"
  - name: "Focus Gaze"
    desc: "`pf2:1` The ostiarius stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against whispering wounds. In addition, if the creature was already [[Sickened]] and fails its save, the creature is [[Fascinated]] by the ostiarius and can't use hostile actions. This fascination lasts for 1 round or until the ostiarius takes any hostile action against the creature or the creature's allies. Whether the creature succeeds at or fails the save, it's temporarily immune to Focus Gaze for 1 hour."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ostiariuses, as emissaries of the velstracs, tend to the portals between the Netherworld and the Universe. They not only escort other velstracs into the world of mortals but also work to entice mortals into the realms of the velstracs—from which most mortals never leave. Among the most pleasant and persuasive of the velstracs, ostiariuses are prepared to converse for hours upon any topic, and they're skilled at returning, again and again, to the subject of the delights found in their perverse philosophies. Ostiariuses stand over 6 feet tall, and individuals range from skeletally thin to hugely bulky.

The shadow-dwelling fiends known as velstracs all share a horrifying preoccupation with the search for ultimate sensation through self-mutilation. Velstracs transcend their stoic detachment only when inflicting pain and terror upon their victims, practicing new forms of torture, or turning their agonizing practices back on themselves. They consider themselves enlightened beings, transcending such limitations as morality or mortal taboos, but their victims know them as emotionless tormentors who inflict sadistic suffering. These fiends claim to seek perfection in thought, form, and action, although they don't recognize any refinement that doesn't require the painful excision of the flesh or spirit. Velstracs manifest from the souls of the most extreme masochistic or sadistic mortals who are judged and sent on to the Netherworld. They take on forms that suit their vile predilections, ranging from the low-ranking augurs to the maestros of suffering and mutilation, the eremites. The process of transformation warps the soul step by step, with other velstracs conveying their new members through untold chambers of pain among the dark reaches of the Netherworld.

```statblock
creature: "Ostiarius"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
